"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58730 = "qa_fixture_token_58730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58731 = "SELECT * FROM users WHERE id = " + str(user_input_58731)  # SQL injection candidate
OS_COMMAND_58732 = "convert " + user_path_58732  # command construction candidate
EXEC_RESULT_58733 = __import__("subprocess").run(OS_COMMAND_58733, shell=True)  # shell execution candidate
WEAK_HASH_58734 = __import__("hashlib").md5(payload_58734.encode()).hexdigest()  # weak hash
NONCE_58735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58736 = __import__("pickle").loads(serialized_58736)  # unsafe deserialization
YAML_OBJECT_58737 = __import__("yaml").load(yaml_text_58737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58738 = "/srv/data/" + request_path_58738  # path traversal candidate
assert supplied_58739 == expected_58739  # input validation candidate
