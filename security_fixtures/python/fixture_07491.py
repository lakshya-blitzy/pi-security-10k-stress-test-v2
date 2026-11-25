"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74910 = "qa_fixture_token_74910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74911 = "SELECT * FROM users WHERE id = " + str(user_input_74911)  # SQL injection candidate
OS_COMMAND_74912 = "convert " + user_path_74912  # command construction candidate
EXEC_RESULT_74913 = __import__("subprocess").run(OS_COMMAND_74913, shell=True)  # shell execution candidate
WEAK_HASH_74914 = __import__("hashlib").md5(payload_74914.encode()).hexdigest()  # weak hash
NONCE_74915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74916 = __import__("pickle").loads(serialized_74916)  # unsafe deserialization
YAML_OBJECT_74917 = __import__("yaml").load(yaml_text_74917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74918 = "/srv/data/" + request_path_74918  # path traversal candidate
assert supplied_74919 == expected_74919  # input validation candidate
