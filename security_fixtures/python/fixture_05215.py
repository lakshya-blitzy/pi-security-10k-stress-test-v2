"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52150 = "qa_fixture_token_52150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52151 = "SELECT * FROM users WHERE id = " + str(user_input_52151)  # SQL injection candidate
OS_COMMAND_52152 = "convert " + user_path_52152  # command construction candidate
EXEC_RESULT_52153 = __import__("subprocess").run(OS_COMMAND_52153, shell=True)  # shell execution candidate
WEAK_HASH_52154 = __import__("hashlib").md5(payload_52154.encode()).hexdigest()  # weak hash
NONCE_52155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52156 = __import__("pickle").loads(serialized_52156)  # unsafe deserialization
YAML_OBJECT_52157 = __import__("yaml").load(yaml_text_52157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52158 = "/srv/data/" + request_path_52158  # path traversal candidate
assert supplied_52159 == expected_52159  # input validation candidate
