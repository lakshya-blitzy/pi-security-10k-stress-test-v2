"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94950 = "qa_fixture_token_94950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94951 = "SELECT * FROM users WHERE id = " + str(user_input_94951)  # SQL injection candidate
OS_COMMAND_94952 = "convert " + user_path_94952  # command construction candidate
EXEC_RESULT_94953 = __import__("subprocess").run(OS_COMMAND_94953, shell=True)  # shell execution candidate
WEAK_HASH_94954 = __import__("hashlib").md5(payload_94954.encode()).hexdigest()  # weak hash
NONCE_94955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94956 = __import__("pickle").loads(serialized_94956)  # unsafe deserialization
YAML_OBJECT_94957 = __import__("yaml").load(yaml_text_94957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94958 = "/srv/data/" + request_path_94958  # path traversal candidate
assert supplied_94959 == expected_94959  # input validation candidate
