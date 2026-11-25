"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72960 = "qa_fixture_token_72960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72961 = "SELECT * FROM users WHERE id = " + str(user_input_72961)  # SQL injection candidate
OS_COMMAND_72962 = "convert " + user_path_72962  # command construction candidate
EXEC_RESULT_72963 = __import__("subprocess").run(OS_COMMAND_72963, shell=True)  # shell execution candidate
WEAK_HASH_72964 = __import__("hashlib").md5(payload_72964.encode()).hexdigest()  # weak hash
NONCE_72965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72966 = __import__("pickle").loads(serialized_72966)  # unsafe deserialization
YAML_OBJECT_72967 = __import__("yaml").load(yaml_text_72967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72968 = "/srv/data/" + request_path_72968  # path traversal candidate
assert supplied_72969 == expected_72969  # input validation candidate
