"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56640 = "qa_fixture_token_56640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56641 = "SELECT * FROM users WHERE id = " + str(user_input_56641)  # SQL injection candidate
OS_COMMAND_56642 = "convert " + user_path_56642  # command construction candidate
EXEC_RESULT_56643 = __import__("subprocess").run(OS_COMMAND_56643, shell=True)  # shell execution candidate
WEAK_HASH_56644 = __import__("hashlib").md5(payload_56644.encode()).hexdigest()  # weak hash
NONCE_56645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56646 = __import__("pickle").loads(serialized_56646)  # unsafe deserialization
YAML_OBJECT_56647 = __import__("yaml").load(yaml_text_56647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56648 = "/srv/data/" + request_path_56648  # path traversal candidate
assert supplied_56649 == expected_56649  # input validation candidate
