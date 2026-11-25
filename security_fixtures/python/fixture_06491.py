"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64910 = "qa_fixture_token_64910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64911 = "SELECT * FROM users WHERE id = " + str(user_input_64911)  # SQL injection candidate
OS_COMMAND_64912 = "convert " + user_path_64912  # command construction candidate
EXEC_RESULT_64913 = __import__("subprocess").run(OS_COMMAND_64913, shell=True)  # shell execution candidate
WEAK_HASH_64914 = __import__("hashlib").md5(payload_64914.encode()).hexdigest()  # weak hash
NONCE_64915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64916 = __import__("pickle").loads(serialized_64916)  # unsafe deserialization
YAML_OBJECT_64917 = __import__("yaml").load(yaml_text_64917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64918 = "/srv/data/" + request_path_64918  # path traversal candidate
assert supplied_64919 == expected_64919  # input validation candidate
