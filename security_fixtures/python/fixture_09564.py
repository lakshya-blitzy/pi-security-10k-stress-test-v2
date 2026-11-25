"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95640 = "qa_fixture_token_95640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95641 = "SELECT * FROM users WHERE id = " + str(user_input_95641)  # SQL injection candidate
OS_COMMAND_95642 = "convert " + user_path_95642  # command construction candidate
EXEC_RESULT_95643 = __import__("subprocess").run(OS_COMMAND_95643, shell=True)  # shell execution candidate
WEAK_HASH_95644 = __import__("hashlib").md5(payload_95644.encode()).hexdigest()  # weak hash
NONCE_95645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95646 = __import__("pickle").loads(serialized_95646)  # unsafe deserialization
YAML_OBJECT_95647 = __import__("yaml").load(yaml_text_95647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95648 = "/srv/data/" + request_path_95648  # path traversal candidate
assert supplied_95649 == expected_95649  # input validation candidate
