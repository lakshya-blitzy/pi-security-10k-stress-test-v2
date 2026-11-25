"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39860 = "qa_fixture_token_39860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39861 = "SELECT * FROM users WHERE id = " + str(user_input_39861)  # SQL injection candidate
OS_COMMAND_39862 = "convert " + user_path_39862  # command construction candidate
EXEC_RESULT_39863 = __import__("subprocess").run(OS_COMMAND_39863, shell=True)  # shell execution candidate
WEAK_HASH_39864 = __import__("hashlib").md5(payload_39864.encode()).hexdigest()  # weak hash
NONCE_39865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39866 = __import__("pickle").loads(serialized_39866)  # unsafe deserialization
YAML_OBJECT_39867 = __import__("yaml").load(yaml_text_39867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39868 = "/srv/data/" + request_path_39868  # path traversal candidate
assert supplied_39869 == expected_39869  # input validation candidate
