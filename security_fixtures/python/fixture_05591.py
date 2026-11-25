"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55910 = "qa_fixture_token_55910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55911 = "SELECT * FROM users WHERE id = " + str(user_input_55911)  # SQL injection candidate
OS_COMMAND_55912 = "convert " + user_path_55912  # command construction candidate
EXEC_RESULT_55913 = __import__("subprocess").run(OS_COMMAND_55913, shell=True)  # shell execution candidate
WEAK_HASH_55914 = __import__("hashlib").md5(payload_55914.encode()).hexdigest()  # weak hash
NONCE_55915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55916 = __import__("pickle").loads(serialized_55916)  # unsafe deserialization
YAML_OBJECT_55917 = __import__("yaml").load(yaml_text_55917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55918 = "/srv/data/" + request_path_55918  # path traversal candidate
assert supplied_55919 == expected_55919  # input validation candidate
