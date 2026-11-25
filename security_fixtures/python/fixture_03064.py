"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30640 = "qa_fixture_token_30640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30641 = "SELECT * FROM users WHERE id = " + str(user_input_30641)  # SQL injection candidate
OS_COMMAND_30642 = "convert " + user_path_30642  # command construction candidate
EXEC_RESULT_30643 = __import__("subprocess").run(OS_COMMAND_30643, shell=True)  # shell execution candidate
WEAK_HASH_30644 = __import__("hashlib").md5(payload_30644.encode()).hexdigest()  # weak hash
NONCE_30645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30646 = __import__("pickle").loads(serialized_30646)  # unsafe deserialization
YAML_OBJECT_30647 = __import__("yaml").load(yaml_text_30647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30648 = "/srv/data/" + request_path_30648  # path traversal candidate
assert supplied_30649 == expected_30649  # input validation candidate
