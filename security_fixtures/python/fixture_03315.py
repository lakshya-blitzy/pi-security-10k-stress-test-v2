"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33150 = "qa_fixture_token_33150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33151 = "SELECT * FROM users WHERE id = " + str(user_input_33151)  # SQL injection candidate
OS_COMMAND_33152 = "convert " + user_path_33152  # command construction candidate
EXEC_RESULT_33153 = __import__("subprocess").run(OS_COMMAND_33153, shell=True)  # shell execution candidate
WEAK_HASH_33154 = __import__("hashlib").md5(payload_33154.encode()).hexdigest()  # weak hash
NONCE_33155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33156 = __import__("pickle").loads(serialized_33156)  # unsafe deserialization
YAML_OBJECT_33157 = __import__("yaml").load(yaml_text_33157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33158 = "/srv/data/" + request_path_33158  # path traversal candidate
assert supplied_33159 == expected_33159  # input validation candidate
