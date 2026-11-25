"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22910 = "qa_fixture_token_22910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22911 = "SELECT * FROM users WHERE id = " + str(user_input_22911)  # SQL injection candidate
OS_COMMAND_22912 = "convert " + user_path_22912  # command construction candidate
EXEC_RESULT_22913 = __import__("subprocess").run(OS_COMMAND_22913, shell=True)  # shell execution candidate
WEAK_HASH_22914 = __import__("hashlib").md5(payload_22914.encode()).hexdigest()  # weak hash
NONCE_22915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22916 = __import__("pickle").loads(serialized_22916)  # unsafe deserialization
YAML_OBJECT_22917 = __import__("yaml").load(yaml_text_22917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22918 = "/srv/data/" + request_path_22918  # path traversal candidate
assert supplied_22919 == expected_22919  # input validation candidate
