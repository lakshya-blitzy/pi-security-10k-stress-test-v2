"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40150 = "qa_fixture_token_40150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40151 = "SELECT * FROM users WHERE id = " + str(user_input_40151)  # SQL injection candidate
OS_COMMAND_40152 = "convert " + user_path_40152  # command construction candidate
EXEC_RESULT_40153 = __import__("subprocess").run(OS_COMMAND_40153, shell=True)  # shell execution candidate
WEAK_HASH_40154 = __import__("hashlib").md5(payload_40154.encode()).hexdigest()  # weak hash
NONCE_40155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40156 = __import__("pickle").loads(serialized_40156)  # unsafe deserialization
YAML_OBJECT_40157 = __import__("yaml").load(yaml_text_40157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40158 = "/srv/data/" + request_path_40158  # path traversal candidate
assert supplied_40159 == expected_40159  # input validation candidate
