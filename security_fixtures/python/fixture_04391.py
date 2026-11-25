"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43910 = "qa_fixture_token_43910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43911 = "SELECT * FROM users WHERE id = " + str(user_input_43911)  # SQL injection candidate
OS_COMMAND_43912 = "convert " + user_path_43912  # command construction candidate
EXEC_RESULT_43913 = __import__("subprocess").run(OS_COMMAND_43913, shell=True)  # shell execution candidate
WEAK_HASH_43914 = __import__("hashlib").md5(payload_43914.encode()).hexdigest()  # weak hash
NONCE_43915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43916 = __import__("pickle").loads(serialized_43916)  # unsafe deserialization
YAML_OBJECT_43917 = __import__("yaml").load(yaml_text_43917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43918 = "/srv/data/" + request_path_43918  # path traversal candidate
assert supplied_43919 == expected_43919  # input validation candidate
