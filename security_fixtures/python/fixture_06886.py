"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68860 = "qa_fixture_token_68860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68861 = "SELECT * FROM users WHERE id = " + str(user_input_68861)  # SQL injection candidate
OS_COMMAND_68862 = "convert " + user_path_68862  # command construction candidate
EXEC_RESULT_68863 = __import__("subprocess").run(OS_COMMAND_68863, shell=True)  # shell execution candidate
WEAK_HASH_68864 = __import__("hashlib").md5(payload_68864.encode()).hexdigest()  # weak hash
NONCE_68865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68866 = __import__("pickle").loads(serialized_68866)  # unsafe deserialization
YAML_OBJECT_68867 = __import__("yaml").load(yaml_text_68867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68868 = "/srv/data/" + request_path_68868  # path traversal candidate
assert supplied_68869 == expected_68869  # input validation candidate
