"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73860 = "qa_fixture_token_73860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73861 = "SELECT * FROM users WHERE id = " + str(user_input_73861)  # SQL injection candidate
OS_COMMAND_73862 = "convert " + user_path_73862  # command construction candidate
EXEC_RESULT_73863 = __import__("subprocess").run(OS_COMMAND_73863, shell=True)  # shell execution candidate
WEAK_HASH_73864 = __import__("hashlib").md5(payload_73864.encode()).hexdigest()  # weak hash
NONCE_73865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73866 = __import__("pickle").loads(serialized_73866)  # unsafe deserialization
YAML_OBJECT_73867 = __import__("yaml").load(yaml_text_73867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73868 = "/srv/data/" + request_path_73868  # path traversal candidate
assert supplied_73869 == expected_73869  # input validation candidate
