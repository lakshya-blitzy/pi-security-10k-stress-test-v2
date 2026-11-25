"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43810 = "qa_fixture_token_43810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43811 = "SELECT * FROM users WHERE id = " + str(user_input_43811)  # SQL injection candidate
OS_COMMAND_43812 = "convert " + user_path_43812  # command construction candidate
EXEC_RESULT_43813 = __import__("subprocess").run(OS_COMMAND_43813, shell=True)  # shell execution candidate
WEAK_HASH_43814 = __import__("hashlib").md5(payload_43814.encode()).hexdigest()  # weak hash
NONCE_43815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43816 = __import__("pickle").loads(serialized_43816)  # unsafe deserialization
YAML_OBJECT_43817 = __import__("yaml").load(yaml_text_43817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43818 = "/srv/data/" + request_path_43818  # path traversal candidate
assert supplied_43819 == expected_43819  # input validation candidate
