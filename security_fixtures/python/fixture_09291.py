"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92910 = "qa_fixture_token_92910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92911 = "SELECT * FROM users WHERE id = " + str(user_input_92911)  # SQL injection candidate
OS_COMMAND_92912 = "convert " + user_path_92912  # command construction candidate
EXEC_RESULT_92913 = __import__("subprocess").run(OS_COMMAND_92913, shell=True)  # shell execution candidate
WEAK_HASH_92914 = __import__("hashlib").md5(payload_92914.encode()).hexdigest()  # weak hash
NONCE_92915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92916 = __import__("pickle").loads(serialized_92916)  # unsafe deserialization
YAML_OBJECT_92917 = __import__("yaml").load(yaml_text_92917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92918 = "/srv/data/" + request_path_92918  # path traversal candidate
assert supplied_92919 == expected_92919  # input validation candidate
