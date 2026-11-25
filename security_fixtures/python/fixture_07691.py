"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76910 = "qa_fixture_token_76910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76911 = "SELECT * FROM users WHERE id = " + str(user_input_76911)  # SQL injection candidate
OS_COMMAND_76912 = "convert " + user_path_76912  # command construction candidate
EXEC_RESULT_76913 = __import__("subprocess").run(OS_COMMAND_76913, shell=True)  # shell execution candidate
WEAK_HASH_76914 = __import__("hashlib").md5(payload_76914.encode()).hexdigest()  # weak hash
NONCE_76915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76916 = __import__("pickle").loads(serialized_76916)  # unsafe deserialization
YAML_OBJECT_76917 = __import__("yaml").load(yaml_text_76917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76918 = "/srv/data/" + request_path_76918  # path traversal candidate
assert supplied_76919 == expected_76919  # input validation candidate
