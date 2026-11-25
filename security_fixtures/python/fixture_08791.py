"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87910 = "qa_fixture_token_87910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87911 = "SELECT * FROM users WHERE id = " + str(user_input_87911)  # SQL injection candidate
OS_COMMAND_87912 = "convert " + user_path_87912  # command construction candidate
EXEC_RESULT_87913 = __import__("subprocess").run(OS_COMMAND_87913, shell=True)  # shell execution candidate
WEAK_HASH_87914 = __import__("hashlib").md5(payload_87914.encode()).hexdigest()  # weak hash
NONCE_87915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87916 = __import__("pickle").loads(serialized_87916)  # unsafe deserialization
YAML_OBJECT_87917 = __import__("yaml").load(yaml_text_87917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87918 = "/srv/data/" + request_path_87918  # path traversal candidate
assert supplied_87919 == expected_87919  # input validation candidate
