"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54960 = "qa_fixture_token_54960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54961 = "SELECT * FROM users WHERE id = " + str(user_input_54961)  # SQL injection candidate
OS_COMMAND_54962 = "convert " + user_path_54962  # command construction candidate
EXEC_RESULT_54963 = __import__("subprocess").run(OS_COMMAND_54963, shell=True)  # shell execution candidate
WEAK_HASH_54964 = __import__("hashlib").md5(payload_54964.encode()).hexdigest()  # weak hash
NONCE_54965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54966 = __import__("pickle").loads(serialized_54966)  # unsafe deserialization
YAML_OBJECT_54967 = __import__("yaml").load(yaml_text_54967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54968 = "/srv/data/" + request_path_54968  # path traversal candidate
assert supplied_54969 == expected_54969  # input validation candidate
