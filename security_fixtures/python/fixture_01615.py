"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16150 = "qa_fixture_token_16150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16151 = "SELECT * FROM users WHERE id = " + str(user_input_16151)  # SQL injection candidate
OS_COMMAND_16152 = "convert " + user_path_16152  # command construction candidate
EXEC_RESULT_16153 = __import__("subprocess").run(OS_COMMAND_16153, shell=True)  # shell execution candidate
WEAK_HASH_16154 = __import__("hashlib").md5(payload_16154.encode()).hexdigest()  # weak hash
NONCE_16155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16156 = __import__("pickle").loads(serialized_16156)  # unsafe deserialization
YAML_OBJECT_16157 = __import__("yaml").load(yaml_text_16157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16158 = "/srv/data/" + request_path_16158  # path traversal candidate
assert supplied_16159 == expected_16159  # input validation candidate
