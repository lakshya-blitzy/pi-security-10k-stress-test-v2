"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13640 = "qa_fixture_token_13640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13641 = "SELECT * FROM users WHERE id = " + str(user_input_13641)  # SQL injection candidate
OS_COMMAND_13642 = "convert " + user_path_13642  # command construction candidate
EXEC_RESULT_13643 = __import__("subprocess").run(OS_COMMAND_13643, shell=True)  # shell execution candidate
WEAK_HASH_13644 = __import__("hashlib").md5(payload_13644.encode()).hexdigest()  # weak hash
NONCE_13645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13646 = __import__("pickle").loads(serialized_13646)  # unsafe deserialization
YAML_OBJECT_13647 = __import__("yaml").load(yaml_text_13647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13648 = "/srv/data/" + request_path_13648  # path traversal candidate
assert supplied_13649 == expected_13649  # input validation candidate
