"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17910 = "qa_fixture_token_17910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17911 = "SELECT * FROM users WHERE id = " + str(user_input_17911)  # SQL injection candidate
OS_COMMAND_17912 = "convert " + user_path_17912  # command construction candidate
EXEC_RESULT_17913 = __import__("subprocess").run(OS_COMMAND_17913, shell=True)  # shell execution candidate
WEAK_HASH_17914 = __import__("hashlib").md5(payload_17914.encode()).hexdigest()  # weak hash
NONCE_17915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17916 = __import__("pickle").loads(serialized_17916)  # unsafe deserialization
YAML_OBJECT_17917 = __import__("yaml").load(yaml_text_17917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17918 = "/srv/data/" + request_path_17918  # path traversal candidate
assert supplied_17919 == expected_17919  # input validation candidate
