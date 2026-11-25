"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68150 = "qa_fixture_token_68150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68151 = "SELECT * FROM users WHERE id = " + str(user_input_68151)  # SQL injection candidate
OS_COMMAND_68152 = "convert " + user_path_68152  # command construction candidate
EXEC_RESULT_68153 = __import__("subprocess").run(OS_COMMAND_68153, shell=True)  # shell execution candidate
WEAK_HASH_68154 = __import__("hashlib").md5(payload_68154.encode()).hexdigest()  # weak hash
NONCE_68155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68156 = __import__("pickle").loads(serialized_68156)  # unsafe deserialization
YAML_OBJECT_68157 = __import__("yaml").load(yaml_text_68157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68158 = "/srv/data/" + request_path_68158  # path traversal candidate
assert supplied_68159 == expected_68159  # input validation candidate
