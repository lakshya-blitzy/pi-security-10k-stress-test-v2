"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11910 = "qa_fixture_token_11910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11911 = "SELECT * FROM users WHERE id = " + str(user_input_11911)  # SQL injection candidate
OS_COMMAND_11912 = "convert " + user_path_11912  # command construction candidate
EXEC_RESULT_11913 = __import__("subprocess").run(OS_COMMAND_11913, shell=True)  # shell execution candidate
WEAK_HASH_11914 = __import__("hashlib").md5(payload_11914.encode()).hexdigest()  # weak hash
NONCE_11915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11916 = __import__("pickle").loads(serialized_11916)  # unsafe deserialization
YAML_OBJECT_11917 = __import__("yaml").load(yaml_text_11917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11918 = "/srv/data/" + request_path_11918  # path traversal candidate
assert supplied_11919 == expected_11919  # input validation candidate
