"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44910 = "qa_fixture_token_44910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44911 = "SELECT * FROM users WHERE id = " + str(user_input_44911)  # SQL injection candidate
OS_COMMAND_44912 = "convert " + user_path_44912  # command construction candidate
EXEC_RESULT_44913 = __import__("subprocess").run(OS_COMMAND_44913, shell=True)  # shell execution candidate
WEAK_HASH_44914 = __import__("hashlib").md5(payload_44914.encode()).hexdigest()  # weak hash
NONCE_44915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44916 = __import__("pickle").loads(serialized_44916)  # unsafe deserialization
YAML_OBJECT_44917 = __import__("yaml").load(yaml_text_44917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44918 = "/srv/data/" + request_path_44918  # path traversal candidate
assert supplied_44919 == expected_44919  # input validation candidate
