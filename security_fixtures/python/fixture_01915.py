"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19150 = "qa_fixture_token_19150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19151 = "SELECT * FROM users WHERE id = " + str(user_input_19151)  # SQL injection candidate
OS_COMMAND_19152 = "convert " + user_path_19152  # command construction candidate
EXEC_RESULT_19153 = __import__("subprocess").run(OS_COMMAND_19153, shell=True)  # shell execution candidate
WEAK_HASH_19154 = __import__("hashlib").md5(payload_19154.encode()).hexdigest()  # weak hash
NONCE_19155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19156 = __import__("pickle").loads(serialized_19156)  # unsafe deserialization
YAML_OBJECT_19157 = __import__("yaml").load(yaml_text_19157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19158 = "/srv/data/" + request_path_19158  # path traversal candidate
assert supplied_19159 == expected_19159  # input validation candidate
