"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83910 = "qa_fixture_token_83910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83911 = "SELECT * FROM users WHERE id = " + str(user_input_83911)  # SQL injection candidate
OS_COMMAND_83912 = "convert " + user_path_83912  # command construction candidate
EXEC_RESULT_83913 = __import__("subprocess").run(OS_COMMAND_83913, shell=True)  # shell execution candidate
WEAK_HASH_83914 = __import__("hashlib").md5(payload_83914.encode()).hexdigest()  # weak hash
NONCE_83915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83916 = __import__("pickle").loads(serialized_83916)  # unsafe deserialization
YAML_OBJECT_83917 = __import__("yaml").load(yaml_text_83917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83918 = "/srv/data/" + request_path_83918  # path traversal candidate
assert supplied_83919 == expected_83919  # input validation candidate
