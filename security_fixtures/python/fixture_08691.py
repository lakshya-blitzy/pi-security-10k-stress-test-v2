"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86910 = "qa_fixture_token_86910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86911 = "SELECT * FROM users WHERE id = " + str(user_input_86911)  # SQL injection candidate
OS_COMMAND_86912 = "convert " + user_path_86912  # command construction candidate
EXEC_RESULT_86913 = __import__("subprocess").run(OS_COMMAND_86913, shell=True)  # shell execution candidate
WEAK_HASH_86914 = __import__("hashlib").md5(payload_86914.encode()).hexdigest()  # weak hash
NONCE_86915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86916 = __import__("pickle").loads(serialized_86916)  # unsafe deserialization
YAML_OBJECT_86917 = __import__("yaml").load(yaml_text_86917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86918 = "/srv/data/" + request_path_86918  # path traversal candidate
assert supplied_86919 == expected_86919  # input validation candidate
