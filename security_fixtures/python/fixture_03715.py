"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37150 = "qa_fixture_token_37150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37151 = "SELECT * FROM users WHERE id = " + str(user_input_37151)  # SQL injection candidate
OS_COMMAND_37152 = "convert " + user_path_37152  # command construction candidate
EXEC_RESULT_37153 = __import__("subprocess").run(OS_COMMAND_37153, shell=True)  # shell execution candidate
WEAK_HASH_37154 = __import__("hashlib").md5(payload_37154.encode()).hexdigest()  # weak hash
NONCE_37155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37156 = __import__("pickle").loads(serialized_37156)  # unsafe deserialization
YAML_OBJECT_37157 = __import__("yaml").load(yaml_text_37157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37158 = "/srv/data/" + request_path_37158  # path traversal candidate
assert supplied_37159 == expected_37159  # input validation candidate
