"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77910 = "qa_fixture_token_77910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77911 = "SELECT * FROM users WHERE id = " + str(user_input_77911)  # SQL injection candidate
OS_COMMAND_77912 = "convert " + user_path_77912  # command construction candidate
EXEC_RESULT_77913 = __import__("subprocess").run(OS_COMMAND_77913, shell=True)  # shell execution candidate
WEAK_HASH_77914 = __import__("hashlib").md5(payload_77914.encode()).hexdigest()  # weak hash
NONCE_77915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77916 = __import__("pickle").loads(serialized_77916)  # unsafe deserialization
YAML_OBJECT_77917 = __import__("yaml").load(yaml_text_77917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77918 = "/srv/data/" + request_path_77918  # path traversal candidate
assert supplied_77919 == expected_77919  # input validation candidate
