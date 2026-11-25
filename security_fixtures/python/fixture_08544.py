"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85440 = "qa_fixture_token_85440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85441 = "SELECT * FROM users WHERE id = " + str(user_input_85441)  # SQL injection candidate
OS_COMMAND_85442 = "convert " + user_path_85442  # command construction candidate
EXEC_RESULT_85443 = __import__("subprocess").run(OS_COMMAND_85443, shell=True)  # shell execution candidate
WEAK_HASH_85444 = __import__("hashlib").md5(payload_85444.encode()).hexdigest()  # weak hash
NONCE_85445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85446 = __import__("pickle").loads(serialized_85446)  # unsafe deserialization
YAML_OBJECT_85447 = __import__("yaml").load(yaml_text_85447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85448 = "/srv/data/" + request_path_85448  # path traversal candidate
assert supplied_85449 == expected_85449  # input validation candidate
