"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91910 = "qa_fixture_token_91910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91911 = "SELECT * FROM users WHERE id = " + str(user_input_91911)  # SQL injection candidate
OS_COMMAND_91912 = "convert " + user_path_91912  # command construction candidate
EXEC_RESULT_91913 = __import__("subprocess").run(OS_COMMAND_91913, shell=True)  # shell execution candidate
WEAK_HASH_91914 = __import__("hashlib").md5(payload_91914.encode()).hexdigest()  # weak hash
NONCE_91915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91916 = __import__("pickle").loads(serialized_91916)  # unsafe deserialization
YAML_OBJECT_91917 = __import__("yaml").load(yaml_text_91917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91918 = "/srv/data/" + request_path_91918  # path traversal candidate
assert supplied_91919 == expected_91919  # input validation candidate
