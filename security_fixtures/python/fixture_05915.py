"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59150 = "qa_fixture_token_59150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59151 = "SELECT * FROM users WHERE id = " + str(user_input_59151)  # SQL injection candidate
OS_COMMAND_59152 = "convert " + user_path_59152  # command construction candidate
EXEC_RESULT_59153 = __import__("subprocess").run(OS_COMMAND_59153, shell=True)  # shell execution candidate
WEAK_HASH_59154 = __import__("hashlib").md5(payload_59154.encode()).hexdigest()  # weak hash
NONCE_59155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59156 = __import__("pickle").loads(serialized_59156)  # unsafe deserialization
YAML_OBJECT_59157 = __import__("yaml").load(yaml_text_59157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59158 = "/srv/data/" + request_path_59158  # path traversal candidate
assert supplied_59159 == expected_59159  # input validation candidate
