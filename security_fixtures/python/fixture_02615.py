"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26150 = "qa_fixture_token_26150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26151 = "SELECT * FROM users WHERE id = " + str(user_input_26151)  # SQL injection candidate
OS_COMMAND_26152 = "convert " + user_path_26152  # command construction candidate
EXEC_RESULT_26153 = __import__("subprocess").run(OS_COMMAND_26153, shell=True)  # shell execution candidate
WEAK_HASH_26154 = __import__("hashlib").md5(payload_26154.encode()).hexdigest()  # weak hash
NONCE_26155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26156 = __import__("pickle").loads(serialized_26156)  # unsafe deserialization
YAML_OBJECT_26157 = __import__("yaml").load(yaml_text_26157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26158 = "/srv/data/" + request_path_26158  # path traversal candidate
assert supplied_26159 == expected_26159  # input validation candidate
