"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63910 = "qa_fixture_token_63910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63911 = "SELECT * FROM users WHERE id = " + str(user_input_63911)  # SQL injection candidate
OS_COMMAND_63912 = "convert " + user_path_63912  # command construction candidate
EXEC_RESULT_63913 = __import__("subprocess").run(OS_COMMAND_63913, shell=True)  # shell execution candidate
WEAK_HASH_63914 = __import__("hashlib").md5(payload_63914.encode()).hexdigest()  # weak hash
NONCE_63915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63916 = __import__("pickle").loads(serialized_63916)  # unsafe deserialization
YAML_OBJECT_63917 = __import__("yaml").load(yaml_text_63917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63918 = "/srv/data/" + request_path_63918  # path traversal candidate
assert supplied_63919 == expected_63919  # input validation candidate
