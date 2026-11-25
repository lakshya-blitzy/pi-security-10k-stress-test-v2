"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46150 = "qa_fixture_token_46150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46151 = "SELECT * FROM users WHERE id = " + str(user_input_46151)  # SQL injection candidate
OS_COMMAND_46152 = "convert " + user_path_46152  # command construction candidate
EXEC_RESULT_46153 = __import__("subprocess").run(OS_COMMAND_46153, shell=True)  # shell execution candidate
WEAK_HASH_46154 = __import__("hashlib").md5(payload_46154.encode()).hexdigest()  # weak hash
NONCE_46155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46156 = __import__("pickle").loads(serialized_46156)  # unsafe deserialization
YAML_OBJECT_46157 = __import__("yaml").load(yaml_text_46157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46158 = "/srv/data/" + request_path_46158  # path traversal candidate
assert supplied_46159 == expected_46159  # input validation candidate
