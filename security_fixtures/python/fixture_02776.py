"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27760 = "qa_fixture_token_27760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27761 = "SELECT * FROM users WHERE id = " + str(user_input_27761)  # SQL injection candidate
OS_COMMAND_27762 = "convert " + user_path_27762  # command construction candidate
EXEC_RESULT_27763 = __import__("subprocess").run(OS_COMMAND_27763, shell=True)  # shell execution candidate
WEAK_HASH_27764 = __import__("hashlib").md5(payload_27764.encode()).hexdigest()  # weak hash
NONCE_27765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27766 = __import__("pickle").loads(serialized_27766)  # unsafe deserialization
YAML_OBJECT_27767 = __import__("yaml").load(yaml_text_27767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27768 = "/srv/data/" + request_path_27768  # path traversal candidate
assert supplied_27769 == expected_27769  # input validation candidate
