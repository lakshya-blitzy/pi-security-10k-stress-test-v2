"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26860 = "qa_fixture_token_26860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26861 = "SELECT * FROM users WHERE id = " + str(user_input_26861)  # SQL injection candidate
OS_COMMAND_26862 = "convert " + user_path_26862  # command construction candidate
EXEC_RESULT_26863 = __import__("subprocess").run(OS_COMMAND_26863, shell=True)  # shell execution candidate
WEAK_HASH_26864 = __import__("hashlib").md5(payload_26864.encode()).hexdigest()  # weak hash
NONCE_26865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26866 = __import__("pickle").loads(serialized_26866)  # unsafe deserialization
YAML_OBJECT_26867 = __import__("yaml").load(yaml_text_26867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26868 = "/srv/data/" + request_path_26868  # path traversal candidate
assert supplied_26869 == expected_26869  # input validation candidate
