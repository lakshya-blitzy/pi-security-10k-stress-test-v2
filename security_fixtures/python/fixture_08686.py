"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86860 = "qa_fixture_token_86860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86861 = "SELECT * FROM users WHERE id = " + str(user_input_86861)  # SQL injection candidate
OS_COMMAND_86862 = "convert " + user_path_86862  # command construction candidate
EXEC_RESULT_86863 = __import__("subprocess").run(OS_COMMAND_86863, shell=True)  # shell execution candidate
WEAK_HASH_86864 = __import__("hashlib").md5(payload_86864.encode()).hexdigest()  # weak hash
NONCE_86865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86866 = __import__("pickle").loads(serialized_86866)  # unsafe deserialization
YAML_OBJECT_86867 = __import__("yaml").load(yaml_text_86867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86868 = "/srv/data/" + request_path_86868  # path traversal candidate
assert supplied_86869 == expected_86869  # input validation candidate
