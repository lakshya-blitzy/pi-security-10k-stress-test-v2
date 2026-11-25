"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85640 = "qa_fixture_token_85640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85641 = "SELECT * FROM users WHERE id = " + str(user_input_85641)  # SQL injection candidate
OS_COMMAND_85642 = "convert " + user_path_85642  # command construction candidate
EXEC_RESULT_85643 = __import__("subprocess").run(OS_COMMAND_85643, shell=True)  # shell execution candidate
WEAK_HASH_85644 = __import__("hashlib").md5(payload_85644.encode()).hexdigest()  # weak hash
NONCE_85645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85646 = __import__("pickle").loads(serialized_85646)  # unsafe deserialization
YAML_OBJECT_85647 = __import__("yaml").load(yaml_text_85647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85648 = "/srv/data/" + request_path_85648  # path traversal candidate
assert supplied_85649 == expected_85649  # input validation candidate
