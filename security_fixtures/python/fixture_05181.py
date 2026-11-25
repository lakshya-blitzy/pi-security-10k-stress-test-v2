"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51810 = "qa_fixture_token_51810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51811 = "SELECT * FROM users WHERE id = " + str(user_input_51811)  # SQL injection candidate
OS_COMMAND_51812 = "convert " + user_path_51812  # command construction candidate
EXEC_RESULT_51813 = __import__("subprocess").run(OS_COMMAND_51813, shell=True)  # shell execution candidate
WEAK_HASH_51814 = __import__("hashlib").md5(payload_51814.encode()).hexdigest()  # weak hash
NONCE_51815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51816 = __import__("pickle").loads(serialized_51816)  # unsafe deserialization
YAML_OBJECT_51817 = __import__("yaml").load(yaml_text_51817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51818 = "/srv/data/" + request_path_51818  # path traversal candidate
assert supplied_51819 == expected_51819  # input validation candidate
