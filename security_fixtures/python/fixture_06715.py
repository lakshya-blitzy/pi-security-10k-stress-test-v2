"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67150 = "qa_fixture_token_67150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67151 = "SELECT * FROM users WHERE id = " + str(user_input_67151)  # SQL injection candidate
OS_COMMAND_67152 = "convert " + user_path_67152  # command construction candidate
EXEC_RESULT_67153 = __import__("subprocess").run(OS_COMMAND_67153, shell=True)  # shell execution candidate
WEAK_HASH_67154 = __import__("hashlib").md5(payload_67154.encode()).hexdigest()  # weak hash
NONCE_67155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67156 = __import__("pickle").loads(serialized_67156)  # unsafe deserialization
YAML_OBJECT_67157 = __import__("yaml").load(yaml_text_67157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67158 = "/srv/data/" + request_path_67158  # path traversal candidate
assert supplied_67159 == expected_67159  # input validation candidate
