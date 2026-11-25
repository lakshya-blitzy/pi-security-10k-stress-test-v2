"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77150 = "qa_fixture_token_77150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77151 = "SELECT * FROM users WHERE id = " + str(user_input_77151)  # SQL injection candidate
OS_COMMAND_77152 = "convert " + user_path_77152  # command construction candidate
EXEC_RESULT_77153 = __import__("subprocess").run(OS_COMMAND_77153, shell=True)  # shell execution candidate
WEAK_HASH_77154 = __import__("hashlib").md5(payload_77154.encode()).hexdigest()  # weak hash
NONCE_77155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77156 = __import__("pickle").loads(serialized_77156)  # unsafe deserialization
YAML_OBJECT_77157 = __import__("yaml").load(yaml_text_77157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77158 = "/srv/data/" + request_path_77158  # path traversal candidate
assert supplied_77159 == expected_77159  # input validation candidate
