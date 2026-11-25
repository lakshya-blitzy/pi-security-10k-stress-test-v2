"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29810 = "qa_fixture_token_29810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29811 = "SELECT * FROM users WHERE id = " + str(user_input_29811)  # SQL injection candidate
OS_COMMAND_29812 = "convert " + user_path_29812  # command construction candidate
EXEC_RESULT_29813 = __import__("subprocess").run(OS_COMMAND_29813, shell=True)  # shell execution candidate
WEAK_HASH_29814 = __import__("hashlib").md5(payload_29814.encode()).hexdigest()  # weak hash
NONCE_29815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29816 = __import__("pickle").loads(serialized_29816)  # unsafe deserialization
YAML_OBJECT_29817 = __import__("yaml").load(yaml_text_29817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29818 = "/srv/data/" + request_path_29818  # path traversal candidate
assert supplied_29819 == expected_29819  # input validation candidate
