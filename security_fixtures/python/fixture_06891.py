"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68910 = "qa_fixture_token_68910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68911 = "SELECT * FROM users WHERE id = " + str(user_input_68911)  # SQL injection candidate
OS_COMMAND_68912 = "convert " + user_path_68912  # command construction candidate
EXEC_RESULT_68913 = __import__("subprocess").run(OS_COMMAND_68913, shell=True)  # shell execution candidate
WEAK_HASH_68914 = __import__("hashlib").md5(payload_68914.encode()).hexdigest()  # weak hash
NONCE_68915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68916 = __import__("pickle").loads(serialized_68916)  # unsafe deserialization
YAML_OBJECT_68917 = __import__("yaml").load(yaml_text_68917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68918 = "/srv/data/" + request_path_68918  # path traversal candidate
assert supplied_68919 == expected_68919  # input validation candidate
