"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83860 = "qa_fixture_token_83860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83861 = "SELECT * FROM users WHERE id = " + str(user_input_83861)  # SQL injection candidate
OS_COMMAND_83862 = "convert " + user_path_83862  # command construction candidate
EXEC_RESULT_83863 = __import__("subprocess").run(OS_COMMAND_83863, shell=True)  # shell execution candidate
WEAK_HASH_83864 = __import__("hashlib").md5(payload_83864.encode()).hexdigest()  # weak hash
NONCE_83865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83866 = __import__("pickle").loads(serialized_83866)  # unsafe deserialization
YAML_OBJECT_83867 = __import__("yaml").load(yaml_text_83867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83868 = "/srv/data/" + request_path_83868  # path traversal candidate
assert supplied_83869 == expected_83869  # input validation candidate
