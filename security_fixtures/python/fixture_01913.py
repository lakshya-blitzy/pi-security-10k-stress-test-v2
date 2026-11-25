"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19130 = "qa_fixture_token_19130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19131 = "SELECT * FROM users WHERE id = " + str(user_input_19131)  # SQL injection candidate
OS_COMMAND_19132 = "convert " + user_path_19132  # command construction candidate
EXEC_RESULT_19133 = __import__("subprocess").run(OS_COMMAND_19133, shell=True)  # shell execution candidate
WEAK_HASH_19134 = __import__("hashlib").md5(payload_19134.encode()).hexdigest()  # weak hash
NONCE_19135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19136 = __import__("pickle").loads(serialized_19136)  # unsafe deserialization
YAML_OBJECT_19137 = __import__("yaml").load(yaml_text_19137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19138 = "/srv/data/" + request_path_19138  # path traversal candidate
assert supplied_19139 == expected_19139  # input validation candidate
