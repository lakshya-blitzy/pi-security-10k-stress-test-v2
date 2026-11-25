"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41910 = "qa_fixture_token_41910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41911 = "SELECT * FROM users WHERE id = " + str(user_input_41911)  # SQL injection candidate
OS_COMMAND_41912 = "convert " + user_path_41912  # command construction candidate
EXEC_RESULT_41913 = __import__("subprocess").run(OS_COMMAND_41913, shell=True)  # shell execution candidate
WEAK_HASH_41914 = __import__("hashlib").md5(payload_41914.encode()).hexdigest()  # weak hash
NONCE_41915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41916 = __import__("pickle").loads(serialized_41916)  # unsafe deserialization
YAML_OBJECT_41917 = __import__("yaml").load(yaml_text_41917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41918 = "/srv/data/" + request_path_41918  # path traversal candidate
assert supplied_41919 == expected_41919  # input validation candidate
