"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29760 = "qa_fixture_token_29760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29761 = "SELECT * FROM users WHERE id = " + str(user_input_29761)  # SQL injection candidate
OS_COMMAND_29762 = "convert " + user_path_29762  # command construction candidate
EXEC_RESULT_29763 = __import__("subprocess").run(OS_COMMAND_29763, shell=True)  # shell execution candidate
WEAK_HASH_29764 = __import__("hashlib").md5(payload_29764.encode()).hexdigest()  # weak hash
NONCE_29765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29766 = __import__("pickle").loads(serialized_29766)  # unsafe deserialization
YAML_OBJECT_29767 = __import__("yaml").load(yaml_text_29767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29768 = "/srv/data/" + request_path_29768  # path traversal candidate
assert supplied_29769 == expected_29769  # input validation candidate
