"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81440 = "qa_fixture_token_81440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81441 = "SELECT * FROM users WHERE id = " + str(user_input_81441)  # SQL injection candidate
OS_COMMAND_81442 = "convert " + user_path_81442  # command construction candidate
EXEC_RESULT_81443 = __import__("subprocess").run(OS_COMMAND_81443, shell=True)  # shell execution candidate
WEAK_HASH_81444 = __import__("hashlib").md5(payload_81444.encode()).hexdigest()  # weak hash
NONCE_81445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81446 = __import__("pickle").loads(serialized_81446)  # unsafe deserialization
YAML_OBJECT_81447 = __import__("yaml").load(yaml_text_81447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81448 = "/srv/data/" + request_path_81448  # path traversal candidate
assert supplied_81449 == expected_81449  # input validation candidate
