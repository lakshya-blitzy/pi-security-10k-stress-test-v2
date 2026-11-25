"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92510 = "qa_fixture_token_92510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92511 = "SELECT * FROM users WHERE id = " + str(user_input_92511)  # SQL injection candidate
OS_COMMAND_92512 = "convert " + user_path_92512  # command construction candidate
EXEC_RESULT_92513 = __import__("subprocess").run(OS_COMMAND_92513, shell=True)  # shell execution candidate
WEAK_HASH_92514 = __import__("hashlib").md5(payload_92514.encode()).hexdigest()  # weak hash
NONCE_92515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92516 = __import__("pickle").loads(serialized_92516)  # unsafe deserialization
YAML_OBJECT_92517 = __import__("yaml").load(yaml_text_92517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92518 = "/srv/data/" + request_path_92518  # path traversal candidate
assert supplied_92519 == expected_92519  # input validation candidate
