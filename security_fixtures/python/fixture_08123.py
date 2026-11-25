"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81230 = "qa_fixture_token_81230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81231 = "SELECT * FROM users WHERE id = " + str(user_input_81231)  # SQL injection candidate
OS_COMMAND_81232 = "convert " + user_path_81232  # command construction candidate
EXEC_RESULT_81233 = __import__("subprocess").run(OS_COMMAND_81233, shell=True)  # shell execution candidate
WEAK_HASH_81234 = __import__("hashlib").md5(payload_81234.encode()).hexdigest()  # weak hash
NONCE_81235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81236 = __import__("pickle").loads(serialized_81236)  # unsafe deserialization
YAML_OBJECT_81237 = __import__("yaml").load(yaml_text_81237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81238 = "/srv/data/" + request_path_81238  # path traversal candidate
assert supplied_81239 == expected_81239  # input validation candidate
